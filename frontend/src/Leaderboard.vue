<script setup lang="ts">

</script>

<template>
    <section class="container">
        <div class="status">
            <h1>Weekly 5k leaderboard</h1>
        </div>
        <img src="/leaderboard.png">
    </section>
</template>

<style lang="scss" scoped>
.container {
    gap: 1.5rem;
}

img {
    width: 4rem;
    height: 4rem;
}

.status {
    border: 1px solid rgba(255, 255, 255, 0.2);
    font-size: 1rem;
    border-radius: 15px;
    padding: 0.5rem 1rem;
    width: 100%;
    display: flex;
    gap: 1rem;
    align-items: center;
    background-color: white;
    color: black;
    justify-content: center;
    padding: 1rem;
}

img {
    width: 100%;
    height: 100%;
}

.goal {
    background-color: white;
    color: black;
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 1rem;
}

.text {
    text-align: left;
}

.emoji {
    font-size: 1.5rem;
}

.metrics1 {
    display: flex;
    gap: 0.5rem;
    align-items: center;
    font-size: 1.5rem;

    h1 {
        font-size: 3rem;
        display: inline;
        margin: 0;
    }
}

.metrics2 {
    display: flex;
    flex-direction: row;
    gap: 2rem;

    p {
        margin-top: 0.2rem;
        margin-bottom: 0.2rem;
    }

    >div {
        display: flex;
        flex-direction: column;
        gap: 0;


    }
}
</style>
