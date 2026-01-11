def generate_explanation(result):
    scores = result["scores"]
    reasons = result["reasons"]

    # Confidence calculation
    max_possible = 10
    diff = abs(scores["mern"] - scores["django"])
    confidence = min(100, int((diff / max_possible) * 100))

    explanation = {
        "mern": {"score": scores["mern"], "reasons": reasons["mern"]},
        "django": {"score": scores["django"], "reasons": reasons["django"]},
        "confidence": confidence
    }

    # Verdict
    if scores["mern"] > scores["django"]:
        verdict = (
            "MERN fits your current constraints better due to speed and familiarity. "
            "Django remains a strong option if your priority shifts toward backend depth."
        )
    elif scores["django"] > scores["mern"]:
        verdict = (
            "Django aligns better with long-term backend goals and structure. "
            "MERN is still valid if rapid development becomes your priority."
        )
    else:
        verdict = (
            "Both options fit your needs similarly. Your comfort with the ecosystem "
            "can guide the final choice."
        )

    explanation["verdict"] = verdict

    # 🔥 WHAT-IF SCENARIO (ADD HERE)
    what_if = []

    if scores["mern"] >= scores["django"]:
        what_if.append(
            "If you had more time (3+ months), Django could become a stronger choice "
            "due to its structured backend and built-in features."
        )
    else:
        what_if.append(
            "If your timeline becomes shorter or you focus on rapid MVP delivery, "
            "MERN could be a better fit."
        )

    explanation["what_if"] = what_if

    return explanation
