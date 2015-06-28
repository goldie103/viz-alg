function step(offset) {
    /**
     * Fetches step data from server.
     * @param {number} offset The requested step number, relative to the
     *    current step.
     */
    var curElement = document.getElementById("current-step-no");
    var curNum = Number(curElement.textContent);
    var reqNum = curNum + offset;
    var totalSteps = Number(document.getElementById("total-steps").textContent);

    var nextElement = document.getElementById("next-step");
    var prevElement = document.getElementById("prev-step");

    if (reqNum === totalSteps) {
        nextElement.style = "visibility: hidden;";
    } else {
        nextElement.style = "";
    }

    if (reqNum === 1 ) {
        prevElement.style = "visibility: hidden;";
    } else {
        prevElement.style = "";
    }

    var stepsElement = document.getElementById("viz-steps");
    var curStep = stepsElement.children[curNum - 1];
    var reqStep = stepsElement.children[reqNum - 1];

    curStep.style = "display: none;";
    reqStep.style = "";

    curElement.textContent = reqNum;
}
