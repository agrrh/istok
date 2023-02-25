<script>
  import Group from './groups/Group.svelte';

  export let groups = [];
</script>

<div class="groups grid grid-cols-3">
{#each groups as group}
  <Group name={group}/>
{/each}
</div>
