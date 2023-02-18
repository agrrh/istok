<script>
  import { onMount } from "svelte";

  export let date = true;
	export let time = true;

  let d = new Date();

  $: dateVal = d.toLocaleDateString();
  $: timeVal = d.toLocaleTimeString();

  onMount(() => {
		const interval = setInterval(() => {
			d = new Date();
		}, 1000);

		return () => {
			clearInterval(interval);
		};
	});
</script>

{#if date || time}
<div class="clock">
  <span class="date">
    {#if date}
      {dateVal}
    {/if}
  </span>

  <span class="time">
    {#if time}
      {timeVal}
    {/if}
  </span>

</div>
{/if}
