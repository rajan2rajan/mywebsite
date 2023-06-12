    var modal = document.getElementById("exampleModal");
    let iframecontainer = document.getElementById('iframeContainer'); 
    let showiframe = document.getElementById('showIframe');
    let video_frame; 
    
    
    const closeModal = () => {
        // iframecontainer.innerHTML = ""; 
        if (video_frame != undefined) {
            video_frame.removeAttribute("src"); 
        }

    }
    const deleteVideoFrameSrc = () => {

    }

    const showModal = (youtubeUrl) => {
        //   iframecontainer.innerHTML = `<iframe id="video_frame"  class="video_frame p-0" src="https://www.youtube.com/embed/SIyxjRJ8VNY" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>`; 
          video_frame =  document.getElementById('video_frame');
          video_frame.setAttribute('src', youtubeUrl)
    }


    modal.addEventListener("hide.bs.modal", closeModal);