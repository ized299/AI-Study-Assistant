import {useState} from 'react';

function Quiz({quiz}) {
    const [currentQuestion, setCurrentQuestion] = useState(0)
    const [selectedAnswer, setSelectedAnswer] = useState(null)
    const [score, setScore] = useState(0)
    const [finished, setFinished] = useState(false)
    const [submitted, setSubmitted] = useState(false)

    const question = quiz.questions[currentQuestion]
    const handleAnswer = (option) => {
        setSelectedAnswer(option);
    };
    const handleSubmit = () => {
        if (selectedAnswer === question.answer) {
            setScore(score + 1);
        }
        setSubmitted(true);
    };
    const handleNext = () => {
        if (currentQuestion < quiz.questions.length - 1) {
            setCurrentQuestion(currentQuestion + 1);
            setSelectedAnswer(null);
            setSubmitted(false);
        } else {
            setFinished(true);
        }
    };
    if (finished) {
        return (
            <div>
                <h2>Quiz Finished!</h2>
                <p>You scored {score} out of {quiz.questions.length}</p>
            </div>
        );
    }

    return (
        <div>
            <p>
                Question {currentQuestion + 1} of {quiz.questions.length}
            </p>
            <h2>{question.question}</h2>
            <div>
                {question.options.map((option) => {
                    const isCorrect = option === question.answer;
                    const isSelected = option === selectedAnswer;

                    let className = "";
                    if (submitted) {
                        if (isCorrect) {
                            className = "correct";
                        } else if (isSelected) {
                            className = "incorrect";
                        }
                    }
                    return (
                    <button
                        key={option}
                        onClick={() => handleAnswer(option)}
                        className={className}
                        disabled={submitted}
                    >
                        {option}
                    </button>
                    );
                })}
            </div>

            {submitted && (
                <div>
                    {selectedAnswer === question.answer ? (
                        <p>✅ Correct!</p>
                    ) : ( 
                        <div>
                            <p>❌ Incorrect!</p>
                            <p><strong>Correct Answer: </strong> {question.answer}</p>
                        </div>
                    )}
                    <p><strong>Explanation:</strong>{question.explanation}</p>
                </div>
            )}
            {!submitted ? (
                <button onClick={handleSubmit} disabled={selectedAnswer === null}>
                    Submit Answer
                </button>
            ) : (
            <button onClick={handleNext}>
                {currentQuestion === quiz.questions.length - 1 ? "Finish Quiz" : "Next Question"}
            </button>
            )}
        </div>
            
    );
}

export default Quiz;