<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<script>
  
	let  avatar, fileinput;
	
	const onFileSelected = (e) => {
    let image = e.target.files[0];
    let reader = new FileReader();
    reader.readAsDataURL(image);
    reader.onload = e => {
      avatar = e.target.result
    };
    
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
  

<!-- <label for="file-upload">
	<span type="btn" class="button is-primary is-large">Scan a receipt!</span>
	<input
		  id="file-upload"
		  type="file"
		  alt="camera"
		  accept="image/*"
		  capture="environment"
		  style="display: none"
		  bind:files
		/>
</label> -->