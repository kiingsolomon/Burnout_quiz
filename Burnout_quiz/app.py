from flask import Flask, render_template, request

app = Flask(__name__)

# Questions categorized
questions = {
    "Emotional Indicators": [
        "I feel overwhelmingly exhausted, no matter how much I rest.",
        "I struggle to feel in control of my life and decisions.",
        "I’ve lost confidence in myself and my abilities.",
        "I feel a sense of shame that I can’t fully explain.",
        "Despite my accomplishments, I feel like I’m failing or that something bad is about to happen.",
        "I feel disconnected from my emotions or have difficulty feeling joy or excitement."
    ],
    "Mental Indicators": [
        "I can’t pinpoint when my exhaustion and burnout began.",
        "I feel weighed down by unresolved past experiences and emotions.",
        "I struggle to concentrate or make decisions.",
        "I often feel negative, cynical, or disillusioned about work or life."
    ],
    "Behavioral Indicators": [
        "I feel isolated, unsupported, and alone in my struggles.",
        "I find myself avoiding tasks, responsibilities, or people.",
        "I’m not performing at my usual level, and tasks feel overwhelming.",
        "I frequently put things off because they feel too draining.",
        "I get frustrated or angry more easily than before."
    ],
    "Physical Indicators": [
        "I have trouble sleeping, wake up frequently, or feel unrested even after sleep.",
        "I’m getting sick more often or experiencing persistent headaches, body aches, or stomach issues.",
        "My eating habits have changed noticeably (overeating or loss of appetite).",
        "I often experience muscle tension, headaches, or unexplained physical pain.",
        "I feel physically drained, even when I haven’t done much."
    ]
}

# Scoring guide
def get_burnout_level(score):
    if score <= 4:
        return "You may be experiencing mild stress. Take time to reflect and prioritize self-care."
    elif score <= 9:
        return "You may be in the early stages of burnout. Consider taking steps to address these feelings."
    elif score <= 15:
        return "You’re showing significant signs of burnout. It’s time to seek support and find ways to restore balance."
    else:
        return "You may be experiencing severe burnout. Prioritize seeking help from a mental health professional or support system."

@app.route('/', methods=['GET', 'POST'])
def burnout_quiz():
    if request.method == 'POST':
        selected_answers = request.form.getlist('answers')
        score = len(selected_answers)
        result = get_burnout_level(score)
        return render_template('result.html', score=score, result=result)
    return render_template('quiz.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True)
