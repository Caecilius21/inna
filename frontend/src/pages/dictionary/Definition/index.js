import React from 'react'
import {Stack, Typography, Box, IconButton} from '@material-ui/core'
import {ArrowBack as BackIcon, BookmarkBorder as BookmarkIcon, Border as BookmarkedIcon} from '@material-ui/icons'


const Definition = () => {
    return (
        <>
            <Stack direction='row' justfyContent='space-between'>
                <IconButton>
                    <BackIcon/>
                </IconButton>
                <IconButton>
                    <BookmarkedIcon/>
                </IconButton>
            </Stack>
        </>
    )
}

export default Definition
