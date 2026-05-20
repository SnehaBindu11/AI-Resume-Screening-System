def generate_recommendations(missing_skills):

    recommendations = []

    for skill in missing_skills:

        if skill == "aws":

            recommendations.append(
                "Learn AWS Cloud fundamentals and add cloud-based projects."
            )

        elif skill == "docker":

            recommendations.append(
                "Learn Docker containerization and deployment concepts."
            )

        elif skill == "kubernetes":

            recommendations.append(
                "Understand Kubernetes orchestration and scaling."
            )

        elif skill == "tensorflow":

            recommendations.append(
                "Build Deep Learning and AI projects using TensorFlow."
            )

        elif skill == "nlp":

            recommendations.append(
                "Work on NLP projects using NLTK or spaCy."
            )

        elif skill == "sql":

            recommendations.append(
                "Improve SQL querying and database management skills."
            )

        elif skill == "streamlit":

            recommendations.append(
                "Build and deploy interactive AI web applications using Streamlit."
            )

        elif skill == "github":

            recommendations.append(
                "Improve GitHub portfolio and version control practices."
            )

        else:

            recommendations.append(
                f"Try improving your practical knowledge in {skill}."
            )

    return recommendations