"""Logging and monitoring utilities for Noveum SDK."""

import logging
import time
from functools import wraps
from typing import Any, Callable, Optional

__all__ = ["get_logger", "setup_logging", "log_performance"]


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Get a logger instance.

    Args:
        name: Logger name
        level: Logging level

    Returns:
        Logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Add console handler if not already present
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


def setup_logging(
    level: int = logging.INFO,
    format_string: Optional[str] = None,
) -> None:
    """
    Setup logging for the SDK.

    Args:
        level: Logging level
        format_string: Custom format string
    """
    if format_string is None:
        format_string = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    logging.basicConfig(
        level=level,
        format=format_string,
    )


def log_performance(func: Callable) -> Callable:
    """
    Decorator to log function performance.

    Args:
        func: Function to decorate

    Returns:
        Decorated function
    """
    logger = get_logger(func.__module__)

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            elapsed = time.time() - start_time
            logger.debug(f"{func.__name__} completed in {elapsed:.3f}s")
            return result
        except Exception as e:
            elapsed = time.time() - start_time
            logger.error(f"{func.__name__} failed after {elapsed:.3f}s: {e}")
            raise

    return wrapper


class PerformanceMonitor:
    """Monitor and track performance metrics."""

    def __init__(self, name: str):
        """
        Initialize monitor.

        Args:
            name: Monitor name
        """
        self.name = name
        self.logger = get_logger(f"noveum.monitor.{name}")
        self.metrics: dict = {}

    def record(self, metric_name: str, value: float) -> None:
        """
        Record a metric.

        Args:
            metric_name: Name of the metric
            value: Metric value
        """
        if metric_name not in self.metrics:
            self.metrics[metric_name] = []
        self.metrics[metric_name].append(value)
        self.logger.debug(f"{metric_name}: {value}")

    def get_stats(self, metric_name: str) -> dict:
        """
        Get statistics for a metric.

        Args:
            metric_name: Name of the metric

        Returns:
            Dictionary with statistics
        """
        if metric_name not in self.metrics:
            return {}

        values = self.metrics[metric_name]
        return {
            "count": len(values),
            "total": sum(values),
            "average": sum(values) / len(values),
            "min": min(values),
            "max": max(values),
        }

    def summary(self) -> dict:
        """Get summary of all metrics."""
        return {
            name: self.get_stats(name)
            for name in self.metrics
        }
