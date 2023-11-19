const SERVER = process.env.REACT_APP_SERVER

export const SITEMAP = `${SERVER}/sitemap`
export const ANALYZE = `${SERVER}/analyze`
export const COMPANIES = `${SERVER}/companies`

export const COMPARE = `${SERVER}/compare`
export const COMPATIBLE = `${SERVER}/compatible`


export async function sitemap(url) {
    return fetch(SITEMAP, {
        method: 'POST', 
        headers: {
          'Content-Type': 'application/json' 
        },
        body: JSON.stringify({
            url: url
        })
    }).then(response => {
        return response.json()
    })
}

export async function companies() {
    return fetch(COMPANIES, {
        method: 'GET', 
        headers: {
          'Content-Type': 'application/json' 
        },
    }).then(response => {
        return response.json()
    })
}

export async function analyze(data) {
    return fetch(ANALYZE, {
        method: 'POST', 
        headers: {
          'Content-Type': 'application/json' 
        },
        body: JSON.stringify(data)
    }).then(response => {
        return response.json()
    })
}


export async function compatible(url) {
    return fetch(COMPATIBLE, {
        method: 'POST', 
        headers: {
          'Content-Type': 'application/json' 
        },
        body: JSON.stringify({
            url: url
        })
    }).then(response => {
        return response.json()
        
    })
}

export async function compare(url1, url2) {
    return fetch(COMPARE, {
        method: 'POST', 
        headers: {
          'Content-Type': 'application/json' 
        },
        body: JSON.stringify({
            url1: url1,
            url2: url2
        })
    }).then(response => {
        return response.json()
    })
}