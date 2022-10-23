<style>
  #cameraFileInput {
  display: none;
}

#pictureFromCamera {
  width: 100%;
  height: auto;
  margin-top: 16px;
}

.btn {
  display: inline-block;
  background-color: #00b531;
  color: white;
  padding: 8px 12px;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
}

.btn:hover {
  filter: brightness(0.9);
}
</style>

<meta charset="utf-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<meta name="viewport" content="width=device-width, initial-scale=1" />

<title>Camera in browsers - pixo</title>

<!-- imports the webpage's stylesheet -->
<link rel="stylesheet" href="style.css" />



<body>
<h1>Scan or Import Receipt</h1>

<!-- The `label` is attached to the hidden file input -->
<label for="cameraFileInput">
  <span class="btn">Open camera</span>

  <!-- The hidden file `input` for opening the native camera -->
  <input
    id="cameraFileInput"
    type="file"
    accept="image/*"
    capture="environment"
  />
</label>

<!-- displays the picture uploaded from the native camera -->
<!-- svelte-ignore a11y-missing-attribute -->
<img id="pictureFromCamera" />
</body>



