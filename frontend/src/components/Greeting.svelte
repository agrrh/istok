<script>
	export let data;

  import Hello from './Hello.svelte';
  import Clock from './Clock.svelte';

  // Sample data:
    // greeting:
    //   enabled: true
    //
    //   name: User
    //
    //   options:
    //     daytime: true
    //     date: true
    //     time: true
</script>

<div class="greeting">
{#if data.enabled}
  <Hello name={data.name} daytime={data.options.daytime}/>
  <Clock date={data.options.date} time={data.options.time}/>
{/if}
</div>
