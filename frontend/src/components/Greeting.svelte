<script>
	export let greeting;

	import Hello from './greeting/Hello.svelte';
	import Clock from './greeting/Clock.svelte';
</script>

<div class="greeting pb-8 mt-16">
{#if greeting.enabled}
	<Hello name={greeting.name} daytime={greeting.options.daytime}/>
	<Clock weekday={greeting.options.weekday} date={greeting.options.date} clock={greeting.options.clock}/>
{/if}
</div>
