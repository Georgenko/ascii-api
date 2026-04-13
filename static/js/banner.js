async function loadBannerFonts() {
    const cyrillic = document.getElementById("checkbox-cyrillic").checked;

    try {
        const data = await getFonts(cyrillic);
        populateFontSelect(data.fonts);
    } catch (err) {
        console.error("Failed to load fonts:", err);
    }
}

function populateFontSelect(fonts) {
    const select = document.getElementById("select-font");
    select.innerHTML = '';

    const fragment = document.createDocumentFragment();
    fonts.forEach((font) => {
        const option = document.createElement('option');
        option.value = font;
        option.textContent = font;
        fragment.appendChild(option);
    });
    select.appendChild(fragment);
}

loadBannerFonts();

async function convertTextToBanner() {
    const input = document.getElementById("textarea-banner").value;
    const font = document.getElementById("select-font").value;
    const cyrillic = document.getElementById("checkbox-cyrillic").checked;
    const request = buildBannerRequest(input, font, cyrillic);

    try {
        const banner = await postTextToBanner(request);
        showResult(banner);
    } catch (err) {
        console.error(err);
    }
}

function buildBannerRequest(prompt, font = "standard", cyrillic = false) {
    return {prompt, font, cyrillic};
}

function showResult(text) {
    document.getElementById("result").textContent = text;
    show('result-view');
}
