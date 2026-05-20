def extract_candidate_name(resume_text):

    lines = resume_text.split("\n")

    for line in lines:

        line = line.strip()

        if len(line.split()) >= 2 and len(line) < 40:
            return line

    return "Candidate"