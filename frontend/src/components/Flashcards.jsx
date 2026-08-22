import {useState} from "react";
function Flashcards({flashcards}) {
    const [currentCard, setCurrentCard] = useState(0);
    const [flipped, setFlipped] = useState(false);

    const card = flashcards.flashcards[currentCard];
    const handleNext = () => {
        if (currentCard < flashcards.flashcards.length - 1) {
            setCurrentCard(currentCard + 1);
            setFlipped(false);
        }
    };
    const handlePrev = () => {
        if (currentCard > 0) {
            setCurrentCard(currentCard - 1);
            setFlipped(false);
        }
    };
    return (
        <div>
            <p>Card {currentCard + 1} of {flashcards.flashcards.length}</p>
            <div><h2>{flipped ? card.back : card.front}</h2></div>

            <button onClick={() => setFlipped(!flipped)}>{flipped ? "Show Question" : "Show Answer"}</button>
            <button onClick={handlePrev} disabled={currentCard === 0}>Previous</button>
            <button onClick={handleNext} disabled={currentCard === flashcards.flashcards.length - 1}>Next</button>
        </div>
    )
}
export default Flashcards;