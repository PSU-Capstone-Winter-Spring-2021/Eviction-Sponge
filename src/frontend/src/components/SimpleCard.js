import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';

import 'react-bootstrap';

export default class SimpleCard extends React.Component{
    constructor(props) {
                super(props);
                this.state = {
                    casenumber : "16LT12205",
                    location: "Jackson",
                    type:"Landlord/Tenant - Residential or Return of Personal Property",
                    status:"closed",
                    eligibility:"Not Eligible"
                  };
    }
    render (){
    return(
    <Container maxWidth="sm">
    <div className = "bg-light">
        {/* <Card className='bg-light '> */}
        <Card className='bg-light text-left'>
            <CardContent>
                <Typography className={this.state.casenumber+" text-center"} color="textSecondary" gutterBottom>
                Type: {this.state.type}
                </Typography>
                <Typography className={this.state.casenumber}  gutterBottom>
                Case#: {this.state.casenumber}
                </Typography>
                <Typography className={this.state.casenumber}  gutterBottom>
                status: {this.state.status}
                </Typography>
                <Typography className={this.state.casenumber}  gutterBottom>
                Location: {this.state.location}
                </Typography>
                <Typography variant="body2" component="p">
                date: 2021-04-26
                {/* API returned incorrect date */}
                </Typography>
                <Typography variant="body2" component="p">
                <Button size="small" className="bg-primary">
                Eligible Now
                </Button>    : {this.state.eligibility}<Button color="primary" variant="contained" size="small">Click to autofill application pdf</Button>
                </Typography>
                <CardActions>
                </CardActions>
            </CardContent>
            </Card>
        </div>
        <br></br>
    </Container>
    );
    }
}