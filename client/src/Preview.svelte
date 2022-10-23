<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<script>
  import { construct_svelte_component } from "svelte/internal";



let avatar, fileinput;
let base64;
let string = "";

const onFileSelected = (e) => {
	let image = e.target.files[0];
	let reader = new FileReader();

	reader.readAsDataURL(image);
	reader.onload = e => {
		avatar = e.target.result
		var string = avatar.toString();
		base64  = avatar.split(',')[1];
		console.log(base64);
		
	}

}

function newReceipt() {
	let query = window.location.search;
  let request_body = {title: string, image: base64}
	console.log(request_body)
	const url = `data/${query.slice(1)}`
  fetch(url, {
		method: "POST",
		body: JSON.stringify(request_body)

	}).then((response) => {response.body.})
		
		//window.location.replace()

}

</script>
<body>
<div class="app">
	<div class = "columns">
	<div class = "column is-one-fifth">
		<h1>Upload or Scan Image</h1>
		<input style="display:none" type="file" accept=".jpg, .jpeg, .png" on:change={(e)=>onFileSelected(e)} bind:this={fileinput} >
	</div>
	<div class = "column is-one-fifth">
	<img class="upload" src="https://static.thenounproject.com/png/625182-200.png" alt="" on:click={()=>{fileinput.click();}} />
	
</div>
<div class = "column is-one-fifth">
<button class="button is-primary is-large" on:click ={()=>{newReceipt()}}>Parse Receipt</button>

<div class = "column is-one-fifth"></div>
	<button  on:click={()=>{fileinput.click()}} class="button is-danger is-large">Retake Image</button>
</div>
</div>

    {#if avatar}

    <img class="avatar" src="{avatar}" alt="d" />

    {:else}

    <img class="avatar" src="https://en.wikipedia.org/wiki/File:Blank_button.svg#/media/File:Blank_button.svg" alt="" /> 
	
    {/if}

	</div>

</body>
<style>

	.app{
		display:flex;
		align-items:center;
		justify-content:center;
		flex-flow:column;
	}

	.upload{
		display:flex;
	height:50px;
		width:50px;
		cursor:pointer;
	}
	.avatar{
		display:flex;
		height:200px;
		width:200px;
	}
</style>
