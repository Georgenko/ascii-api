function buildBannerRequest(prompt, font = "standard", cyrillic = false) {
    return {prompt, font, cyrillic};
}

async function convertTextToBanner() {
    const input = document.querySelector("#text-to-banner input");
    const request = buildBannerRequest(input.value);

    try {
        const banner = await postTextToBanner(request);
        console.log(banner); // swap with DOM rendering later
    } catch (err) {
        console.error(err.message);
    }
}
