const sections = ['text-to-banner', 'image-to-ascii', 'prompt-to-ascii', 'banner-view', 'image-view', 'docs'];
// TODO: extract constants somewhere and reuse throughout JS and maybe HTML/CSS?
const imageSections = ['image-to-ascii', 'prompt-to-ascii'];
let lastSection = 'text-to-banner';

function show(id) {
    sections.forEach(s => document.getElementById(s).hidden = (s !== id));
    if (id !== 'banner-view' && id !== 'image-view') lastSection = id;

    const imageOptions = document.getElementById("image-options")
    if (imageSections.includes(id)) {
        const target = document.getElementById(id);
        const button = target.querySelector("button");
        target.insertBefore(imageOptions, button);
        imageOptions.hidden = false;
    } else {
        imageOptions.hidden = true;
    }
}

show('text-to-banner');

function showResult(result, divElemId) {
    document.querySelector(`#${divElemId} pre`).textContent = result;
    show(divElemId);
}

function getImageOptions() {
    const minimal = document.getElementById("image-minimal").checked;
    let width = document.getElementById("image-width").value;
    let numChars = document.getElementById("image-num-chars").value;

    if (!width) {
        width = 500;
    } else if (width <= 0 || width > 10000) {
        alert("Please enter a Width > 0 and <= 10000");
        return null;
    }

    if (!minimal) {
        if (!numChars) {
            alert("Please enter a Number of characters when non-minimal");
            return null;
        }
        if (numChars <= 0 || numChars > 70) {
            alert("Please enter a Number of characters > 0 and <= 70");
            return null;
        }
    } else {
        numChars = 70;
    }

    return { minimal, width, numChars };
}
