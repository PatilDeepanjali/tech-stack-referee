def compare_stacks(user):
    """
    user: dict with keys
    - background
    - time
    - goal
    - budget
    """

    scores = {
        "mern": 0,
        "django": 0
    }

    reasons = {
        "mern": [],
        "django": []
    }

    # 1. Programming background
    if user["background"] == "javascript":
        scores["mern"] += 2
        reasons["mern"].append("JavaScript experience aligns well with MERN stack.")
    elif user["background"] == "python":
        scores["django"] += 2
        reasons["django"].append("Python background makes Django easier to adopt.")
    else:
        scores["mern"] += 1
        scores["django"] += 1
        reasons["mern"].append("Beginner-friendly frontend ecosystem.")
        reasons["django"].append("Structured backend helps beginners learn fundamentals.")

    # 2. Time availability
    if user["time"] == "short":
        scores["mern"] += 2
        reasons["mern"].append("Faster setup and rapid development for short timelines.")
    elif user["time"] == "long":
        scores["django"] += 2
        reasons["django"].append("More time allows learning Django’s structured backend.")

    # 3. Project goal
    if user["goal"] == "college":
        scores["mern"] += 1
        reasons["mern"].append("Popular choice for college projects and demos.")
    elif user["goal"] == "mvp":
        scores["mern"] += 2
        reasons["mern"].append("Quick MVP development with minimal setup.")
    elif user["goal"] == "backend":
        scores["django"] += 2
        reasons["django"].append("Strong backend architecture and built-in features.")

    # 4. Budget
    if user["budget"] == "low":
        scores["mern"] += 1
        scores["django"] += 1
        reasons["mern"].append("Works well with free-tier tools and services.")
        reasons["django"].append("Open-source and cost-effective backend framework.")

    return {
        "scores": scores,
        "reasons": reasons
    }
def compare_stacks(user):
    """
    user: dict with keys
    - background
    - time
    - goal
    - budget
    """

    scores = {
        "mern": 0,
        "django": 0
    }

    reasons = {
        "mern": [],
        "django": []
    }

    # 1. Programming background
    if user["background"] == "javascript":
        scores["mern"] += 2
        reasons["mern"].append("JavaScript experience aligns well with MERN stack.")
    elif user["background"] == "python":
        scores["django"] += 2
        reasons["django"].append("Python background makes Django easier to adopt.")
    else:
        scores["mern"] += 1
        scores["django"] += 1
        reasons["mern"].append("Beginner-friendly frontend ecosystem.")
        reasons["django"].append("Structured backend helps beginners learn fundamentals.")

    # 2. Time availability
    if user["time"] == "short":
        scores["mern"] += 2
        reasons["mern"].append("Faster setup and rapid development for short timelines.")
    elif user["time"] == "long":
        scores["django"] += 2
        reasons["django"].append("More time allows learning Django’s structured backend.")

    # 3. Project goal
    if user["goal"] == "college":
        scores["mern"] += 1
        reasons["mern"].append("Popular choice for college projects and demos.")
    elif user["goal"] == "mvp":
        scores["mern"] += 2
        reasons["mern"].append("Quick MVP development with minimal setup.")
    elif user["goal"] == "backend":
        scores["django"] += 2
        reasons["django"].append("Strong backend architecture and built-in features.")

    # 4. Budget
    if user["budget"] == "low":
        scores["mern"] += 1
        scores["django"] += 1
        reasons["mern"].append("Works well with free-tier tools and services.")
        reasons["django"].append("Open-source and cost-effective backend framework.")

    return {
        "scores": scores,
        "reasons": reasons
    }
