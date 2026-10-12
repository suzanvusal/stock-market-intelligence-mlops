"""A modest, chronological baseline experiment; not a trading strategy."""
from __future__ import annotations

import warnings

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, balanced_accuracy_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

FEATURE_COLUMNS = ["daily_return", "sma_20", "sma_50", "rsi_14", "macd", "macd_signal", "volatility_20d_annualized"]


def evaluate_baseline(features: pd.DataFrame) -> dict[str, float | int | str]:
    """Evaluate a logistic regression on chronological holdout data.

    Predictors come from session t and the target is the direction from close t to close t+1;
    this models an after-close research exercise, not an intraday execution strategy. Requires enough rows after indicator warm-up.
    """
    frame = features.copy()
    frame["target"] = (frame["Close"].shift(-1) > frame["Close"]).astype("int64")
    frame.loc[frame.index[-1], "target"] = float("nan")
    # On row t, the features used to predict the next session are those known at t.
    usable = frame[FEATURE_COLUMNS].copy()
    usable = usable.replace([float("inf"), float("-inf")], float("nan"))
    usable["target"] = frame["target"]
    usable = usable.dropna()
    if len(usable) < 80 or usable["target"].nunique() < 2:
        return {"status": "insufficient_data", "samples": len(usable)}

    split = int(len(usable) * 0.8)
    train, test = usable.iloc[:split], usable.iloc[split:]
    if train["target"].nunique() < 2 or test.empty:
        return {"status": "insufficient_class_balance", "samples": len(usable)}
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000, random_state=42))
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        model.fit(train[FEATURE_COLUMNS], train["target"])
    predictions = model.predict(test[FEATURE_COLUMNS])
    return {
        "status": "ok",
        "samples": len(usable),
        "train_samples": len(train),
        "test_samples": len(test),
        "accuracy": round(float(accuracy_score(test["target"], predictions)), 4),
        "balanced_accuracy": round(float(balanced_accuracy_score(test["target"], predictions)), 4),
        "baseline_up_rate": round(float(test["target"].mean()), 4),
    }
