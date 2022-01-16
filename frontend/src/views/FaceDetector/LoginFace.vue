<template>
  <div class="page">
    <!-- <video
      id="video"
      width="720"
      height="560"
      autoplay
      muted
      @play="detect()"
    ></video> -->
  </div>
</template>
<script>
// import * as faceapi from "face-api.js";
// const MODEL_URL = "/models";
// Promise.all([
//   faceapi.nets.faceLandmark68Net.loadFromUri(MODEL_URL),
//   faceapi.nets.ssdMobilenetv1.loadFromUri(MODEL_URL),
//   faceapi.nets.tinyFaceDetector.loadFromUri(MODEL_URL),
//   faceapi.nets.faceRecognitionNet.loadFromUri(MODEL_URL),
// ]);
// export default {
//   mounted() {
//     this.startVideo();
//   },
//   methods: {
//     startVideo() {
//       const video = document.getElementById("video");
//       navigator.getUserMedia(
//         { video: {} },
//         (stream) => (video.srcObject = stream),
//         (err) => console.error(err)
//       );
//     },
//     detect() {
//       const video = document.getElementById("video");
//       const canvas = faceapi.createCanvasFromMedia(video);
//       setInterval(async () => {
//         const faceMatcher = new faceapi.FaceMatcher(
//           await this.loadLabeledImages(),
//           0.6
//         );
//         const displaySize = { width: video.width, height: video.height };
//         const detection = await faceapi
//           .detectSingleFace(video)
//           .withFaceLandmarks()
//           .withFaceDescriptor();
//         const resizedDetections = faceapi.resizeResults(detection, displaySize);
//         document.body.append(canvas);
//         const result = faceMatcher.findBestMatch(resizedDetections.descriptor);
//         canvas.getContext("2d").clearRect(0, 0, canvas.width, canvas.height);
//         faceapi.draw.drawDetections(canvas, resizedDetections);
//         const box = resizedDetections.detection.box;
//         const drawBox = new faceapi.draw.DrawBox(box, {
//           label: result.toString(),
//         });
//         drawBox.draw(canvas);
//       }, 300);
//     },
//     loadLabeledImages() {
//       const labels = [
//         "ginza",
//         "โหย่ว",
//         "ceo",
//         "somkuan",
//         "siri",
//         "pagard",
//         "กลม",
//       ];
//       return Promise.all(
//         labels.map(async (label) => {
//           const descriptions = [];
//           const img = await faceapi.fetchImage(`./${label}.jpeg`);
//           const detection = await faceapi.detectSingleFace(img).withFaceLandmarks().withFaceDescriptor()
//           descriptions.push(detection.descriptor);
//           return new faceapi.LabeledFaceDescriptors(label, descriptions);
//         })
//       );
//     },
//   },
// };
</script>
<style>
.photo {
  max-width: 200px;
  margin-bottom: 10px;
}
</style>