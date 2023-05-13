export const release = {
    extends: ["semantic-release-config-dt-python-poetry"],
    plugins: [
        [
            "@semantic-release/changelog",
            {
                changelogFile: "docs/CHANGELOG.md",
            },
        ],
        [
            "@semantic-release/git",
            {
                assets: ["docs/CHANGELOG.md"],
            },
        ],
    ],
};
