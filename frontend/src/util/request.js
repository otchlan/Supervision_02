const SERVER = process.env.REACT_APP_SERVER

const SITEMAP = `${SERVER}/sitemap`
const ANALYZE = `${SERVER}/analyze`


export async function sitemap() {
    return fetch(SITEMAP, {
        method: 'GET', 
        headers: {
          'Content-Type': 'application/json' 
        },
    }).then(response => {
        return response.json()
    })
}

export async function analyze() {
    return fetch(ANALYZE, {
        method: 'POST', 
        headers: {
          'Content-Type': 'application/json' 
        },
        body: JSON.stringify({
            url: "example.com"
        })
    }).then(response => {
        return response.json()
    })
}