<script>
  import { onMount } from "svelte";

  export let name = "";

  const endpoint = "http://127.0.0.1:8081/";

  let items = [];

  onMount(async function () {
		var response;
		var data;

		response = await fetch(endpoint + "items/" + name);
		data = await response.json();
		items = data;
	});
</script>


<h3>{name}</h3>

{#if items.length > 0}
  {#each items as item}
    <div class="item">
      <pre>
      #{item.name}  {item.title}
      {item.descr}
      {item.icon}   {item.url}
      </pre>
    </div>
  {/each}
{:else}
  No active items.
{/if}
