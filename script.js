const videoItems = document.querySelectorAll(".video-items video");
let activeIndex = 0;

function updateActiveVideo() {
  console.log("Active video index:", activeIndex);
  videoItems.forEach((video, index) => {
    video.classList.remove("active");
    video.style.width = "320px";
    video.style.height = "240px";
    video.style.transform = "scale(0.9)"; // Reset transformasi

    // Jika video bukan yang aktif, rotasi sedikit
    if (index !== activeIndex) {
      if (index < activeIndex) {
        video.style.transform += " rotateY(-15deg)"; // Video kiri berputar sedikit
      } else {
        video.style.transform += " rotateY(15deg)"; // Video kanan berputar sedikit
      }
    }
  });

  // Set video aktif
  videoItems[activeIndex].classList.add("active");
  console.log("Updated active video:", videoItems[activeIndex]);
}

// Fungsi untuk sebelumnya dan berikutnya
function prevVideo() {
  console.log("Prev button clicked");
  activeIndex = (activeIndex - 1 + videoItems.length) % videoItems.length;
  updateActiveVideo();
}

function nextVideo() {
  console.log("Next button clicked");
  activeIndex = (activeIndex + 1) % videoItems.length;
  updateActiveVideo();
}

// Inisialisasi video awal
updateActiveVideo();
