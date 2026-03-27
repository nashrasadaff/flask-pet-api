let cat_btn=document.getElementById("cat_btn");
let dog_btn=document.getElementById("dog_btn");
let fox_btn=document.getElementById("fox_btn");
let panda_btn=document.getElementById("panda_btn");
let petImg = document.getElementById("petImage"); 
let loader = document.getElementById("loader");
let random_btn = document.getElementById("random_btn");
let history = [];
let historyDiv = document.getElementById("history");
async function loadPet(type) {
    try {
        cat_btn.disabled = true;
        dog_btn.disabled = true;
        fox_btn.disabled = true;
        panda_btn.disabled = true;

        loader.style.display = "block";
        petImg.classList.add("fade-out");

        let response = await fetch(`/${type}`);

        if (!response.ok) throw new Error("Server error");

        let data = await response.json();

        if (data.error) throw new Error(data.error);

        setTimeout(() => {
            petImg.src = data.image;
            petImg.classList.remove("fade-out");
        }, 200);

        petImg.onload = () => {
            loader.style.display = "none";
        };

        petImg.onerror = () => {
            loader.style.display = "none";
            alert("Image failed to load");
        };

        // ✅ history logic
        history.unshift(data.image);

        if (history.length > 5) {
            history.pop();
        }

        historyDiv.innerHTML = "";

        history.forEach(img => {
            let image = document.createElement("img");
            image.src = img;
            image.style.width = "80px";
            image.style.margin = "5px";

            image.onclick = () => {
                petImg.src = img;
            };

            historyDiv.appendChild(image);
        });

    } catch (error) {
        loader.style.display = "none";
        alert(error.message);
        console.error(error);

    } finally {
        cat_btn.disabled = false;
        dog_btn.disabled = false;
        fox_btn.disabled = false;
        panda_btn.disabled = false;
    }
}
random_btn.onclick = () => loadPet("random");
fox_btn.onclick = () => loadPet("fox");
panda_btn.onclick = () => loadPet("panda");
cat_btn.onclick = () => loadPet("cat");
dog_btn.onclick = () => loadPet("dog");




