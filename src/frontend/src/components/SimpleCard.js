import React from 'react';
// import { makeStyles } from 'material-ui/core/styles';
import Card from '@material-ui/core/Card';
// import CardActions from 'material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
// import Button from 'material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import 'react-bootstrap';

export default class SimpleCard extends React.Component{
    constructor(props) {
                super(props);
                this.state = {
                    // casenumber : "16LT12205",
                    // location: "Jackson",
                    // type:"Landlord/Tenant - Residential or Return of Personal Property",
                    // status:"closed",
                    // eligibility:"Not Eligible"
                    result: this.props.res
                  };
    }
    render (){
    console.log("from simple card: ")
    console.log(this.props.res)

    return(
    <div className = "bg-light">
        <Card className='bg-light'>
        <CardContent>
            <Typography className={this.state.casenumber} color="textSecondary" gutterBottom>
            {this.state.result}
            </Typography>
            <Typography className={this.state.casenumber}  gutterBottom>
            Location: {this.state.result.location}
            </Typography>
            <Typography className={this.state.casenumber}  gutterBottom>
            Type: {this.state.result.style}
            </Typography>
            <Typography className={this.state.casenumber}  gutterBottom>
            status: {this.state.result.status}
            </Typography>
            <Typography variant="body2" component="p">
            date: 2021-04-26
            </Typography>
            <Typography variant="body2" component="p">
            eligibility: {this.state.result.eligibility}
            </Typography>
        </CardContent>
        </Card>
    </div>
    );
    }
}