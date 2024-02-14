#!/usr/bin/node

const fetch = require('node-fetch');

async function getCharacters(movieId) {
    try {
        // Fetching movie data
        const movieUrl = `https://swapi.dev/api/films/${movieId}/`;
        const movieResponse = await fetch(movieUrl);
        if (!movieResponse.ok) {
            throw new Error('Error fetching movie data.');
        }

        const movieData = await movieResponse.json();
        const charactersUrls = movieData.characters;

        // Fetching character names
        const characters = [];
        for (const url of charactersUrls) {
            const response = await fetch(url);
            if (!response.ok) {
                console.log(`Error fetching character data from ${url}`);
            } else {
                const characterData = await response.json();
                characters.push(characterData.name);
            }
        }
        return characters;
    } catch (error) {
        console.error(error.message);
        return [];
    }
}

async function main() {
    const args = process.argv.slice(2);
    if (args.length !== 1) {
        console.log('Usage: node script.js <Movie ID>');
        process.exit(1);
    }

    const movieId = args[0];
    const characters = await getCharacters(movieId);

    if (characters.length > 0) {
        characters.forEach(character => console.log(character));
    }
}

main();
