<script>
	import { onMount } from "svelte";

	import dateFormat, { masks } from "dateformat";

	export let weekday = true;
	export let date = true;
	export let clock = true;

	let now = new Date();

	$: delimiter = now.getSeconds() % 2 == 0 ? ":" : " "
	$: weekdayString = dateFormat(now, "dddd");
	$: dateString = dateFormat(now, "mmmm dS");
	$: clockString = dateFormat(now, "HH MM").replace(" ", delimiter);

  onMount(() => {
		const interval = setInterval(() => {
			now = new Date();
		}, 1000);

		return () => {
			clearInterval(interval);
		};
	});
</script>

{#if weekday || date || clock}
<div class="clock items-stretch pb-4 font-sans text-4xl">
	<p>
		{#if weekday}
			{weekdayString},
		{/if}

		{#if date}
			{dateString}
		{/if}
	</p>
	<p>
		{#if clock}
			{clockString}
		{/if}
	</p>
</div>
{/if}
