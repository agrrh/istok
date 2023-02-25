<script>
	import { onMount } from "svelte";
	import urlJoin from 'url-join';

	export let name = "";

	const endpoint = "http://127.0.0.1:8081/";

	let items = [];

	onMount(async function () {
		var response;
		var data;

		var url = urlJoin(endpoint, "items", name);
		response = await fetch(url);
		items = await response.json();
	});
</script>

<div class="group pb-12">
	<span class="text-2xl font-bold capitalize">{name}</span>
	<div class="group-items flex">
		{#if items.length > 0}
			{#each items as item}
				<a
					id="{name}.{item.name}"
					href="{item.url}"
					class="
						item
						grid grid-cols-3
						my-6 mr-8 py-2 pr-4
						rounded-md
						hover:bg-slate-600 hover:no-underline visited:text-slate-400
					"
				>
					<div class="col-span-1 text-4xl capitalize">
						<span class="inline iconify-inline" data-icon="{item.icon}"></span>
					</div>

					<div class="item-content col-span-2">
						<span class="text-xl capitalize">
							{item.title}
						</span>
						<p>
						{item.descr}
						</p>
					</div>
				</a>
			{/each}
		{/if}
	</div>
</div>
