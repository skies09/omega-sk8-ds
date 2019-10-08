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
    "help": "What are you looking for?",

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
    const Question = element("input");
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
