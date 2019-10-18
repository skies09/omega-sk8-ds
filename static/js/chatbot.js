const Evaluate = expression => {
    try {
        if (isLegal(expression)) {
            const result = eval(expression);
            return result;
        }
        else {
            return "error";
        }
    }
    catch (err) {
        return "error";
    }
}

//Answers
const Answers = {
    "hi": "hello",
    "hello": "hi",
    "help": "What are you looking for?",
    "dont know": "Then I cannot help.",
    "what is the free grip tape?": "It is the standard black coloured MOB grip tape",
    "decks": "try the decks page, found by clicking DECKS in the navigation bar",
    "trucks": "try the trucks page, found by clicking TRUCKS in the navigation bar",
    "completes": "try the compleses page, found by clicking COMPLETES in the navigation bar",
    "wheels": "try the wheels page, found by clicking WHEELS in the navigation bar",
    "accessories": "try the accessories page, found by clicking ACCESSORIES in the navigation bar",
    "bearings": "bearings are found in the accessories page",
    "helmet": "helmets are found in the accessories page",
    "grip tape": "grip tape is found in the accessories page",
    "delivery": "information regarding delivery can be found on the delivery and returns page, the link is at the bottom of the page",
    "returns": "information regarding returns can be found on the delivery and returns page, the link is at the bottom of the page",

    



};

const Notfound = "Sorry, I cannot answer that.";

const D = window.document;

const element = selector => D.querySelector(selector);

const Answer = (Main, Text) => {
    let Flag = false;
    const Result = Evaluate(Text);
    text = Text.toLowerCase();
    Object.keys(Answers).forEach(key => {
        if (!Flag) {
            if (text.indexOf(key) !== -1) {
                addAnswer(
                    Main,
                    Answers[key].replace(
                    )
                );
                Flag = true;
            }
            else if (typeof Result == "number") {
                addAnswer(
                    Main,
                    `${Text} equals ${Result}`
                );
                Flag = true;
            }
        }
    });
    if (!Flag) {
        addAnswer(Main, Notfound);
    }
};
const addQuestion = (Main, text) => {
    Main.innerHTML += `
        <div class="row">
            <div class="chat question">${text}</div>
        </div>
    `;
}

const addAnswer = (Main, text) => {
    Main.innerHTML += `
    <div class="row">
        <div class="chat answer">${text}</div>
    </div>
    `;
}

D.addEventListener("DOMContentLoaded", () => {
    const Main = element("main");
    const Askbtn = element("#askbtn");
    const Question = element(".askbar");
    const Lastdiv = element("#last");

    Question.focus();
    const Ask = () => {
        const Text = Question.value;
        if (Text.length) {
            addQuestion(Main, Text);
            Question.value = "";
            Answer(Main, Text);
            Lastdiv.scrollIntoView();
        }
    };

    Askbtn.addEventListener("click", function (event) {
        Ask();
    });
    Question.addEventListener("keyup", function (event) {
        if (event.keyCode === 13) Ask();
    });
});


function openForm() {
    document.getElementById("myForm").style.display = "block";
}

function closeForm() {
    document.getElementById("myForm").style.display = "none";
}
