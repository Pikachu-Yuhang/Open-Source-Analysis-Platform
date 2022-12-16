<template>
    <button class="learn-more">UPDATE</button>
</template>
<script>
export default {
    name: 'ButtonVue',
    props: {
    },
    methods:{

    },

    
}
</script>
<style scoped>
@import url("https://fonts.googleapis.com/css?family=Rubik:700&display=swap");
* {
  box-sizing: border-box;
}
*::before, *::after {
  box-sizing: border-box;
}

body {
  font-family: "Rubik", sans-serif;
  font-size: 1rem;
  line-height: 1.5;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0;
  min-height: 100vh;
  background: #fff;
}

button {
  position: relative;
  display: inline-block;
  cursor: pointer;
  outline: none;
  border: 0;
  vertical-align: middle;
  text-decoration: none;
  font-size: inherit;
  font-family: inherit;
}
button.learn-more {
  font-weight: 600;
  color: #382b22;
  text-transform: uppercase;
  padding: 0.75em 1em;
  background: #c6e5f7;
  border: 2px solid #9289FF;
  border-radius: 0.75em;
  transform-style: preserve-3d;
  transition: transform 150ms cubic-bezier(0, 0, 0.58, 1) background 150ms cubic-bezier(0, 0, 0.58, 1);
}
button.learn-more::before {
  position: absolute;
  content: "";
  width: 100%;
  height: 90%;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: #b4bbf8;
  border-radius: inherit;
  box-shadow: 0 0 0 2px #9289FF, 0 0.625em 0 0 #e2e0fc;
  transform: translate3d(0, 0.75em, -1em);
  transition: transform 150ms cubic-bezier(0, 0, 0.58, 1), box-shadow 150ms cubic-bezier(0, 0, 0.58, 1);
}
button.learn-more:hover {
  background: #afdbf5;
  transform: translate(0, 0.25em);
}
button.learn-more:hover::before {
  box-shadow: 0 0 0 2px #9289FF, 0 0.5em 0 0 #e2e0fc;
  transform: translate3d(0, 0.5em, -1em);
}
button.learn-more:active {
  background: #afdbf5;
  transform: translate(0em, 0.75em);
}
button.learn-more:active::before {
  box-shadow: 0 0 0 2px #9289FF, 0 0 #e2e0fc;
  transform: translate3d(0, 0, -1em);
}
</style>