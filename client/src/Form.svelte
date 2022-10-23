<div class="field">
  <label class="label">Name</label>
  <div class="control">
    <input bind:value={name}>
   
  </div>
</div>


<div class="box">
  {#if (!formfilled)}
  <div class="control">
    <button class="button is-danger" >Submit</button>
  </div>
  {:else}

    <div class="control">
      <button class="button is-primary" on:click = {formProcess()} >Submit</button>
    </div>
  {/if}
</div>


<script>
  $:formfilled = (name.length === 0);
  name = name;
  let name = '';
  var formFilled = false;
  console.log(name);
 
</script>




