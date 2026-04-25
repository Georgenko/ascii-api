async function convertImageToImage(){
    const fileInput = document.querySelector('#image-to-ascii input[type="file"]');
    const file = fileInput.files[0];

    const { minimal, width, numChars } = getImageOptions();

    // TODO: when choosing a width that is 1000 for banana.png i get the bug of shrinking nav section
    // and its text overflows

    if (!file) {
        alert('Please select an image first');
        return;
    }

    const formData = new FormData();
    formData.append('image', file);

    try {
        const imageResult = await postImageToImage(formData, minimal, width, numChars);
        showResult(imageResult, "image-view");
    } catch (err) {
        alert(`Failed to convert image to ascii:\n${err.message}`);
    }
}
