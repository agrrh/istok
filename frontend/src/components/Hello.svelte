<script>
  export let name = 'User';
	export let daytime = true;

  function getDayTime() {
    const titles = [
      "night",
      "morning",
      "day",
      "evening",
    ];
    const intervals = [
      [0, 5],
      [6, 11],
      [12, 17],
      [18, 23],
    ];

    var currentdate = new Date();
    var h = currentdate.getHours();

    var i = 0;
    for (const interval of intervals) {
      if (h >= interval[0] && h <= interval[1]) {
        return titles[i];
      }
      i++;
    }
  }
</script>

<div class="hello">

{#if daytime}
  Good {getDayTime()}, {name}!
{:else}
  Hello, {name}!
{/if}

</div>
