function findMyLocation() {
    console.log("클릭");
    function locationLoadSuccess(pos) {
        const x = pos.coords.latitude;
        const y = pos.coords.longitude;

        const longInput = document.querySelector(".long");
        const latiInput = document.querySelector(".lati");

        latiInput.value = x;
        longInput.value = y;

        console.log(latiInput.value);
        console.log(longInput.value);
    }

    function locationLoadError(pos) {
        alert("위치를 찾을 수 없습니다");
    }

    if (!navigator.geolocation) {
        alert("브라우저에서 위치 찾기 기능을 찾을 수 없습니다")
    } else {
        navigator.geolocation.getCurrentPosition(locationLoadSuccess, locationLoadError);
    }
}


document.querySelector(".find-my-loc").addEventListener("click", findMyLocation);