<script>
	import { onMount } from "svelte";

	import Greeting from './components/Greeting.svelte';
	import GroupsList from './components/GroupsList.svelte';

	const endpoint = "http://127.0.0.1:8081/";

	export let config = {};
	export let greeting = {};
	export let groups = [];

	onMount(async function () {
		var response;
		var data;

		// Config
		response = await fetch(endpoint + "config/");
		config = await response.json();
		greeting = config.greeting;

		// Groups
		response = await fetch(endpoint + "groups/");
		groups = await response.json();
	});
</script>

<div class="grid grid-cols-8 gap-4 place-items-center justify-items-center">
	<aside class="col-span-1"></aside>
	<main class="col-span-6 justify-self-stretch text-slate-400 accent-slate-200">
		<Greeting greeting={greeting}/>
		<GroupsList groups={groups}/>
	</main>
	<aside class="col-span-1"></aside>
</div>
