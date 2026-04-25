const sections = ['text-to-banner', 'image-to-ascii', 'prompt-to-ascii', 'banner-view', 'image-view'];
// TODO: extract constants somewhere and reuse throughout JS and maybe HTML/CSS?
let lastSection = 'text-to-banner';

function show(id) {
    sections.forEach(s => document.getElementById(s).hidden = (s !== id));
    if (id !== 'banner-view' && id !== 'image-view') lastSection = id;
}

show('text-to-banner');

function showResult(result, preElemId, divElemId) {
    // TODO: see if you can get the pre element from the div, so you can reduce args to 2
    document.getElementById(preElemId).textContent = result;
    show(divElemId);
}
