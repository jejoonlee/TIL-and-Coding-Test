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


function loading() {
    console.log("정보 가지고 오기")
    alert("Open API 와이파이 정보를 가지고 오는 중입니다\n시간이 걸릴 수도 있습니다\n시작을 하기 위해 확인을 눌러주세요");
}

document.querySelector(".update-data").addEventListener("click", loading);
document.querySelector(".find-my-loc").addEventListener("click", findMyLocation);