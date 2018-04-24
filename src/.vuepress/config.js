module.exports = {
    title: 'ACM at FSU',
    description: 'See our event calendar on Facebook:',
    head: [
        ['link', { rel: 'icon', href: `/favicon.png` }]
    ],
    themeConfig: {
        nav: [
            { text: 'Home', link: '/' },
            { text: 'Facebook', link: 'https://facebook.com/ACMatFSU' },
            { text: 'Slack', link: 'https://acmatfsu.slack.com' },
        ],
        search: false,
    }
}
