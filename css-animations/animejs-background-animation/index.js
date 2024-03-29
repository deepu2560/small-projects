const container = document.querySelector(".container");

for (let index = 0; index < 100; index++) {
    const blocks = document.createElement("div");
    blocks.classList.add("block");
    container.appendChild(blocks);
}

function animateBlocks(){
    anime({
        targets: ".block",
        translateX: function(){
            return anime.random(-700, 700)
        },
        translateY: function(){
            return anime.random(-500, 500)
        },
        scale: function(){
            return anime.random(1, 5)
        },
        easing: "linear",
        duration: 3000,
        delay: anime.stagger(10),
        complete: animateBlocks,
    })
}

animateBlocks()