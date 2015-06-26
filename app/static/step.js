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
        nextElement.classList.add("hidden");
    } else {
        nextElement.classList.remove("hidden");
    }

    if (reqNum === 1 ) {
        prevElement.classList.add("hidden");
    } else {
        prevElement.classList.remove("hidden");
    }

    var stepsElement = document.getElementById("viz-steps");
    var curStep = stepsElement.children[curNum - 1];
    var reqStep = stepsElement.children[reqNum - 1];

    curStep.classList.remove("shown");
    curStep.classList.add("hidden");

    reqStep.classList.remove("hidden");
    reqStep.classList.add("shown");

    curElement.textContent = reqNum;
}
