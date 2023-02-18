<script>
  import Group from './Group.svelte';

  export let data = [];
</script>

{#each data as group}
  <Group name={group}/>
{/each}
