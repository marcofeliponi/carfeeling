<template>
    <div class="rating">
      <label v-for="star in 5" :key="star">
        <NIcon color="#ffcd3c">
          <Star v-if="star <= roundedValue" />
          <StarHalf v-else-if="star - 0.5 === roundedValue" />
          <StarOutline v-else />
        </NIcon>
      </label>
    </div>
  </template>

<script>

import { Star, StarHalf, StarOutline } from '@vicons/ionicons5';
import { NIcon } from 'naive-ui';

export default {
    name: "StarRating",

    components: {
        NIcon,
        Star,
        StarHalf,
        StarOutline
    },

    props: {
        value: {
            type: Number,
            default: 0,
        },
    },

    computed: {
    roundedValue() {
      return Math.round(this.value * 2) / 2;
    },
  },
};
</script>

<style scoped>
.rating {
  display: flex;
  direction: row-reverse;
}

.rating {
  margin-top: 5px;
  font-size: 2.5em;
}


</style>