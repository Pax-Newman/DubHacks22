
  <div class="field">
  <label class="label">Name</label>
  <div class="control">
    <input bind:value={name}>
   
  </div>
</div>


{#if (typeof name === 'string' && name.length === 0) }
<div class="control">
  <button class="button is-danger" >Submit</button>
</div>
{:else}
  <div class="control">
    <button class="button is-primary" on:click = {checkForm({name})} >Submit</button>
  </div>
{/if}
  
<script>
  import { user } from "./stores";



let name = '';
function checkForm(){
  console.log("in");
  console.log(name);
  if (typeof name === 'string' && name.length === 0){
    console.log("try again");
  }
  user.set(name);
}

 
</script>



