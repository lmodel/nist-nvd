package example;

/* metamodel_version: 1.12.0 */
/* version: 2.2.4 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  One change to a vulnerability's record at NVD.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdChange  {

  private String cveChangeId;
  private String sourceIdentifier;
  private ZonedDateTime created;
  private NvdCve cveId;
  private String eventName;
  private List<NvdChangeDetail> details;


}