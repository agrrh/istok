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
		data = await response.json();
		config = data;
		greeting = config.greeting;

		// Groups
		response = await fetch(endpoint + "groups/");
		data = await response.json();
		groups = data;
	});
</script>

<main>
	<Greeting data={greeting}/>
	<GroupsList data={groups}/>
</main>
